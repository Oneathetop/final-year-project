async function predictStudent(){

    const data = {

        G1: Number(document.getElementById("G1").value),
        G2: Number(document.getElementById("G2").value),
        absences: Number(document.getElementById("absences").value),
        studytime: Number(document.getElementById("studytime").value),
        age: Number(document.getElementById("age").value),
        famrel: Number(document.getElementById("famrel").value),
        freetime: Number(document.getElementById("freetime").value),
        health: Number(document.getElementById("health").value),
        goout: Number(document.getElementById("goout").value),
        failures: Number(document.getElementById("failures").value)

    };

    const res = await fetch("/predict",{

        method: "POST",

        headers:{
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    });

    const result = await res.json();

    if(result.error){
        document.getElementById("result").innerHTML =
        "<b>Error:</b> " + result.error;
        return;
    }

    const risk = result.predicted_risk;

    let color = "#28a745"; // Green (Low)

    if(risk === "Medium"){
        color = "#ffc107"; // Yellow
    }

    if(risk === "High"){
        color = "#dc3545"; // Red
    }

    document.getElementById("result").innerHTML =
        "<b>Predicted Final Grade:</b> " + result.predicted_g3 +
        "<br><br>" +
        "<b>Risk Level:</b> " +
        `<span class="risk-badge" style="background:${color}">${risk}</span>`;
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