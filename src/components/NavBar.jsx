import React from 'react';
import { NavLink } from 'react-router-dom';

export default function NavBar() {
	return(
		<nav>
			<h1>PostureSpotter</h1>
			<NavLink to="/login" className={({ isActive }) => (isActive ? 'active' : '')}>Login (here for testing)</NavLink>
			<NavLink to="/" className={({ isActive }) => (isActive ? 'active' : '')}>Home</NavLink>
		</nav>
	);
}