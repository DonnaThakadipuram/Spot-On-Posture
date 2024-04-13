export default function WorkoutCard({workout}) {
	return (
		<div className="workoutCard">
			<img className="workoutImage" src="" alt="Placeholder" width="300" height="200" />
			<div className="workoutCardDesc">
				<h2>{workout}</h2>
			</div>
		</div>
	);
}