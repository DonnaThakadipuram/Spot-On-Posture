import { NavLink } from "react-router-dom";

const Login = () => {
	return (
		<div class="container">
			<div class="form-box">
				<h1 id="title">Sign Up</h1>
				<form id="main_form">
					<div class="input-group">
						<div class="input-field" id="nameField">
							<i class="fa-solid fa-user"></i>
							<input type="text" id="fullname" placeholder="Name" />
						</div>
						<div class="input-field">
							<i class="fa-solid fa-envelope"></i>
							<input type="email" id="email" placeholder="Email" />
						</div>
						<div class="input-field">
							<i class="fa-solid fa-lock"></i>
							<input type="password" id="password" placeholder="Password" />
						</div>
						<a href="#">Forgot password?</a>
					</div>
					<div class="btn-field">
						<button type="button" id="signupBtn" class="submit">Sign up</button>
						<button type="button" id="signinBtn" class="disable">Sign in</button>
					</div>
				</form>
			</div>
		</div>
	);
}

export default Login