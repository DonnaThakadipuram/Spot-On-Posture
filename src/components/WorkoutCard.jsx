export default function WorkoutCard({workout}) {
	return (
		<div>
			<div className="workoutCard">
				<img className="workoutImage" src="public/cropped.png" alt="Placeholder" width="300" height="200" />
				<div className="desc">
					<p>{workout}</p>
					<h5>
						Sample text
					</h5>
				</div>
			</div>
		</div>
	);
}