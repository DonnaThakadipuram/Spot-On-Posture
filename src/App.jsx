import { BrowserRouter, Routes, Route } from "react-router-dom"

// pages
import Home from "./pages/Home"
import Login from "./pages/Login";
import Workout from "./pages/Workout";


function App() {
	return (
		<BrowserRouter basename={process.env.PUBLIC_URL}>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/login" element={<Login />} />
				<Route path="/workout" element={<Workout />} />
			</Routes>
		</BrowserRouter>
	);
}

export default App;
