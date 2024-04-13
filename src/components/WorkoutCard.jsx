import { NavLink } from "react-router-dom"

export default function WorkoutCard({workout}) {
	let imgSrc = "./" + workout + ".jpg";
	return (
		<div className="workoutCard">
			<NavLink to="/workout" className={({ isActive }) => (isActive ? 'active' : '')}>
			<img className="workoutImage" src={imgSrc} alt="Placeholder" width="300" height="200" />
			<div className="workoutCardDesc">
				<h2>{workout}</h2>
			</div>
			</NavLink>
		</div>
	);
}