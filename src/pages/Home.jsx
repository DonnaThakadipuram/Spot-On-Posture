import NavBar from "../components/NavBar"
import WorkoutCard from "../components/WorkoutCard"

const Home = () => {

	const workouts = [
		"Deadlift",
		"Squats",
		"Bench"
	]

	return (
		<>
			<NavBar />
			<div className="page home">
				<center>
					<h1>Welcome back, username!</h1>
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