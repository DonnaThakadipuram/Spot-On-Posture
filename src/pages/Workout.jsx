import * as tf from '@tensorflow/tfjs';
import * as tmPose from '@teachablemachine/pose';
import { useEffect } from 'react';

const Workout = () => {
	const URL = "./my_model/";
	let model, webcam, ctx, labelContainer, maxPredictions;

	useEffect(() => {
		setInterval(() => init(), 1000)
	}, [init])

	/*function WebcamImage() {
		const [img, setImg] = useState(null);
		const webcamRef = useRef(null);

		const videoConstraints = {
			width: 420,
			height: 420,
			facingMode: "user",
		};

		const capture = useCallback(() => {
			const imageSrc = webcamRef.current.getScreenshot();
			setImg(imageSrc);
		}, [webcamRef]);

		return (
			<div className="Container">
				{img === null ? (
					<>
						<Webcam
							audio={false}
							mirrored={true}
							height={400}
							width={400}
							ref={webcamRef}
							screenshotFormat="image/jpeg"
							videoConstraints={videoConstraints}
						/>
						<button onClick={capture}>Capture photo</button>
					</>
				) : (
					<>
						<img src={img} alt="screenshot" />
						<button onClick={() => setImg(null)}>Retake</button>
					</>
				)}
			</div>
		);
	}*/

	async function init() {
		const modelURL = URL + "model.json";
		const metadataURL = URL + "metadata.json";

		// load the model and metadata
		// Refer to tmImage.loadFromFiles() in the API to support files from a file picker
		// Note: the pose library adds a tmPose object to your window (window.tmPose)
		model = await tmPose.load(modelURL, metadataURL);
		maxPredictions = model.getTotalClasses();

		// Convenience function to setup a webcam
		const size = 200;
		const flip = false; // whether to flip the webcam
		webcam = new tmPose.Webcam(size, size, flip); // width, height, flip
		await webcam.setup(); // request access to the webcam
		await webcam.play();
		window.requestAnimationFrame(loop);

		// append/get elements to the DOM
		const canvas = document.getElementById("canvas");
		canvas.width = size; canvas.height = size;
		ctx = canvas.getContext("2d");
		labelContainer = document.getElementById("label-container");
		webcam.canvas = canvas;

		for (let i = 0; i < maxPredictions; i++) { // and class labels
			labelContainer.appendChild(document.createElement("div"));
			labelContainer.appendChild(document.createElement("div"));
		}
	}

	async function loop(timestamp) {
		webcam.update(); // update the webcam frame
		await predict();
		window.requestAnimationFrame(loop);
	}

	async function predict() {
		// Prediction #1: run input through posenet
		// estimatePose can take in an image, video or canvas html element
		console.log("hey")
		console.log(webcam);
		const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
		console.log("the other hey")
		// Prediction 2: run input through teachable machine classification model
		const prediction = await model.predict(posenetOutput);

		for (let i = 0; i < maxPredictions; i++) {
			const classPrediction =
				prediction[i].className + ": " + prediction[i].probability.toFixed(2);
			labelContainer.childNodes[i].innerHTML = classPrediction;
		}

		// finally draw the poses
		drawPose(pose);
	}

	function drawPose(pose) {
		if (webcam.canvas) {
			ctx.drawImage(webcam.canvas, 0, 0);
			// draw the keypoints and skeleton
			if (pose) {
				const minPartConfidence = 0.5;
				tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
				tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
			}
		}
	}

	return (
		<div className="page workout">
			<div>Teachable Machine Pose Model</div>
			<button type="button" onClick={init}>Start</button>
			<div>
				<canvas id="canvas"></canvas>
			</div>
			<div id="label-container"></div>
		</div>
	);
}

export default Workout