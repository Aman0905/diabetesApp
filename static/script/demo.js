// Get form inputs

const smoke = document.getElementById("smoke");
const stroke = document.getElementById("stroke");
const heartAttack = document.getElementById("HeartAttack");
const phyAct = document.getElementById("phyact");
const alcohol = document.getElementById("Alcohol");
const genhlt = document.getElementById("Genhlt");
const menhlt = document.getElementById("menhlt");
const Phyhlt = document.getElementById("phyhlt");
const Diffwalk = document.getElementById("DiffWalk");
const Age = document.getElementById("age");
const Education = document.getElementById("education");
const Income = document.getElementById("income");

// Validate input fields

function validBMI() {
  let bmi = document.getElementById("bmi");
  if (bmi.value === "" || isNaN(bmi.value) || bmi.value < 0 || bmi.value > 50) {
    alert("Please enter a valid BMI.");
  }
}

function validMtl() {
  if (
    menhlt.value === "" ||
    isNaN(menhlt.value) ||
    menhlt.value < 0 ||
    menhlt.value > 30
  ) {
    alert("Please enter a valid number for mental health.");
    return false;
  }
}

function validPhyl() {
  if (
    Phyhlt.value === "" ||
    isNaN(Phyhlt.value) ||
    Phyhlt.value < 0 ||
    Phyhlt.value > 30
  ) {
    alert("Please enter a valid number for Physical health.");
    return false;
  }
}

function validAge() {
  if (
    Age.value === "" ||
    isNaN(Age.value) ||
    Age.value < 0 ||
    Age.value > 100
  ) {
    alert("Please enter a valid Age.");
    return false;
  }
}
