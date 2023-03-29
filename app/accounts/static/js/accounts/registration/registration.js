const steps = Array.from(document.querySelectorAll("form .step"));
const nextBtn = document.querySelectorAll("form .next-btn");
const prevBtn = document.querySelectorAll("form .previous-btn");
const form = document.querySelector("form");

document.addEventListener("mousedown", (event) => {
	activateNavigationButtons();
});

document.addEventListener("keypress", (event) => {
	activateNavigationButtons();
});

$("select").on("change", (evt) => {
	$(evt.target).removeClass("invalid");
});

function activateNavigationButtons() {
	let navigationButtons = $(".btn-navigate-form-step");

	Array.from(navigationButtons).forEach((button) => {
		if ($(button).attr("disabled")) {
			console.log("clicked");
			$(button).removeAttr("disabled");
		}
	});
	$("#formErrors").text("");
}
nextBtn.forEach((button) => {
	button.addEventListener("click", () => {
		changeStep("next");
	});
});
prevBtn.forEach((button) => {
	button.addEventListener("click", () => {
		changeStep("prev");
	});
});
form.addEventListener("submit", (e) => {
	e.preventDefault();
	const inputs = [];
	form.querySelectorAll("input").forEach((input) => {
		const { name, value } = input;
		inputs.push({ name, value });
	});
	console.log(inputs);
	form.reset();
});

function isEmptyOrSpaces(str) {
	return str === null || str.match(/^ *$/) !== null;
}

function disableNavigationButtons(step) {
	step.querySelectorAll("button").forEach((button) => {
		button.disabled = true;
	});
}

function setSelectError(name) {
	$(`select[name*=${name}]`).addClass("invalid");
}

function setInputError(name) {
	$(`input[name*=${name}]`).addClass("invalid");
}

function validateIsURL(value) {
	try {
		new URL(value);
		return true;
	} catch (err) {
		return false;
	}
}

function validatePassword(name, value, step) {
	let isValid = true;
	if (!value) {
		isValid = false;
		disableNavigationButtons(step);
		$(`input[name*=${name}]`).addClass("invalid");
	} else {
		if (name === "password1") {
			const regexp = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
			if (!regexp.test(value)) {
				isValid = false;
				disableNavigationButtons(step);
				const msg =
					"Please provide a strong password. The password should have a minimum of 8 characters, have at least one symbol, a number, and a combination of uppercase and lowercase characters.";
				$("#password1Errors").addClass("invalid").text(msg);
			}else{
				isValid = true;
				$("#password1Errors").removeClass("invalid").text("");
			}
		}
		if (name === "password2") {
			const password1 = $("input[name*=password1]").val();
			if (!password1) {
				isValid = false;
				disableNavigationButtons(step);
				$("input[name*=password1]").addClass("invalid");
				$("input[name*=password2]").addClass("invalid");
				$("#password2Errors")
					.addClass("invalid")
					.text("Please set your password.");
			} else {
				if (value !== password1) {
					isValid = false;
					disableNavigationButtons(step);
					$("#password2Errors")
						.addClass("invalid")
						.text("Your passwords don't match.");
				} else {
					isValid = true;
					$("#password2Errors").removeClass("invalid").text("");
				}
			}
		}
	}
	return isValid;
}

function validateStep(step) {
	let isValid = true;
	step.querySelectorAll("input").forEach((input) => {
		const inputs = [];
		const { name, value } = input;
		inputs.push({ name, value });
		inputs.forEach((input) => {
			if (name && $(`input[name*=${name}]`).attr("type") === "password") {
				isValid = validatePassword(name, value, step);
			}
			if (isEmptyOrSpaces(input.value)) {
				setInputError(input.name);
				disableNavigationButtons(step);
				isValid = false;
			} else if (
				name &&
				isValid &&
				$(`input[name*=${name}]`).attr("type") === "url"
			) {
				const isValidURL = validateIsURL(value);
				if (!isValidURL) {
					setInputError(input.name);
					isValid = false;
					disableNavigationButtons(step);
					$(`label[for="${name}"]`).text("Please provide a valid url.");
					$(`label[for="${name}"]`).css("color", "#f44336");
				}
			}
		});
	});
	step.querySelectorAll("select").forEach((input) => {
		const inputs = [];
		const { name, value } = input;
		inputs.push({ name, value });
		console.log(inputs);
		inputs.forEach((input) => {
			if (isEmptyOrSpaces(input.value)) {
				setSelectError(input.name);
				disableNavigationButtons(step);
				isValid = false;
			}
		});
	});
	return isValid;
}

function changeStep(btn) {
	let index = 0;
	const active = document.querySelector(".active-step");
	index = steps.indexOf(active);
	const stepValid = validateStep(steps[index]);
	if (stepValid === true) {
		steps[index].classList.remove("active-step");
		if (btn === "next") {
			index++;
		} else if (btn === "prev") {
			index--;
		}
		steps[index].classList.add("active-step");
	}
}
