import NavBar from "../components/NavBar"
import WorkoutCard from "../components/WorkoutCard"

const Home = () => {

	const workouts = [
		"Deadlift",
		"Squats",
		"Bench Press"
	]

	return (
		<>
			{/* <NavBar /> */}
			<div className="header">
				<h1>Spot-On Posture</h1>
			</div>
			<div className="page home">
				<center>
					<h1 className="title">Welcome back, Ananya!</h1>
					<div className = "workoutCardContainer">
						{workouts.map((workout) => (
							<WorkoutCard workout = {workout}/>
						))}
					</div>
				</center>
			</div>
		</>
	)
}

export default Home