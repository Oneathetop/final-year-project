async function predictStudent(){

    const data = {

        studytime: Number(document.getElementById("studytime").value),
        failures: Number(document.getElementById("failures").value),
        absences: Number(document.getElementById("absences").value)

    };

    const res = await fetch("/predict",{

        method: "POST",

        headers:{
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    });

    const result = await res.json();

    document.getElementById("result").innerHTML =

        "<b>Predicted Final Grade:</b> " + result.predicted_grade +
        "<br><br>" +
        "<b>Risk Level:</b> " + result.risk_level;

}



async function sendCSV(){

    const fileInput = document.getElementById("fileInput");

    if(!fileInput.files.length){

        alert("Please upload a CSV file first.");
        return;

    }

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    const res = await fetch("/predict_csv",{

        method:"POST",
        body:formData

    });

    const data = await res.json();

    document.getElementById("csvResult").textContent = JSON.stringify(data, null, 2);

}