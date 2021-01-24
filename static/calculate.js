function calculate()
{
    var parcel_length = parseFloat(document.getElementById('parcel_length').value);
    var parcel_width = parseFloat(document.getElementById('parcel_width').value);
    var parcel_height = parseFloat(document.getElementById('parcel_height').value);
    var parcel_weight = parseFloat(document.getElementById('parcel_weight').value);
    var overallWeight = (parcel_length*parcel_width*parcel_height)/6000;
    var plan = document.getElementById('standard3').value;
    var parcel_cost = parseFloat(document.getElementById('parcel_cost').value);
    var zabor = 0;
    var dostavka = 0;
    var pricePlan = 0;
    document.getElementById('parcel_dimension').value = overallWeight.toFixed(2).replace(/\.0+$/,'');

<!-- Ekonom Moskva->Tashkent-->
    if (plan == '1')
    {
        if (document.getElementById('parcel_zabor').checked == true) {
            zabor = 6;
        } else if (document.getElementById('parcel_zabor').checked == false) {
            zabor = 0;
        }
        if (document.getElementById('parcel_dostavka').checked == true) {
            dostavka = 6;
        } else if (document.getElementById('parcel_dostavka').checked == false) {
            dostavka = 0;
        }

        pricePlan = 6;
        if (document.getElementById('parcel_weight').value == '')
        {
            parcel_weight = 2;
//            document.getElementById('parcel_weight').value = 2;
            if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }
        else
        {
        if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            }
        }

    }

<!-- Ekonom Tashkent->Moscow-->
    else if (plan == '2')
    {
        if (document.getElementById('parcel_zabor').checked == true) {
            zabor = 2;
        } else if (document.getElementById('parcel_zabor').checked == false) {
            zabor = 0;
        }
        if (document.getElementById('parcel_dostavka').checked == true) {
            dostavka = 2;
        } else if (document.getElementById('parcel_dostavka').checked == false) {
            dostavka = 0;
        }

        pricePlan = 6;
        if (document.getElementById('parcel_weight').value == '')
        {
            parcel_weight = 2;
//            document.getElementById('parcel_weight').value = 2;
            if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }
        else
        {
        if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }

    }


<!-- Standart Moskva->Tashkent-->
    if (plan == '3')
    {
        if (document.getElementById('parcel_zabor').checked == true) {
            zabor = 6;
        } else if (document.getElementById('parcel_zabor').checked == false) {
            zabor = 0;
        }
        if (document.getElementById('parcel_dostavka').checked == true) {
            dostavka = 6;
        } else if (document.getElementById('parcel_dostavka').checked == false) {
            dostavka = 0;
        }

        pricePlan = 12;
        if (document.getElementById('parcel_weight').value == '')
        {
            parcel_weight = 1;
//            document.getElementById('parcel_weight').value = 1;
            if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }
        else
        {
        if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }

    }

<!-- Standart Tashkent->Moscow-->
    else if (plan == '4')
    {
        if (document.getElementById('parcel_zabor').checked == true) {
            zabor = 2;
        } else if (document.getElementById('parcel_zabor').checked == false) {
            zabor = 0;
        }
        if (document.getElementById('parcel_dostavka').checked == true) {
            dostavka = 2;
        } else if (document.getElementById('parcel_dostavka').checked == false) {
            dostavka = 0;
        }

        pricePlan = 11;
        if (document.getElementById('parcel_weight').value == '')
        {
            parcel_weight = 1;
//                        document.getElementById('parcel_weight').value = 1;

            if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }
        else
        {
        if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }

    }


<!-- UltraSrochni Moskva->Tashkent-->
    if (plan == '5')
    {
        if (document.getElementById('parcel_zabor').checked == true) {
            zabor = 6;
        } else if (document.getElementById('parcel_zabor').checked == false) {
            zabor = 0;
        }
        if (document.getElementById('parcel_dostavka').checked == true) {
            dostavka = 6;
        } else if (document.getElementById('parcel_dostavka').checked == false) {
            dostavka = 0;
        }

        pricePlan = 30;
        if (document.getElementById('parcel_weight').value == '')
        {
            parcel_weight = 1;
//                        document.getElementById('parcel_weight').value = 1;

            if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }
        else
        {
        if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }

    }

<!-- Standart Tashkent->Moscow-->
    else if (plan == '6')
    {
        if (document.getElementById('parcel_zabor').checked == true) {
            zabor = 2;
        } else if (document.getElementById('parcel_zabor').checked == false) {
            zabor = 0;
        }
        if (document.getElementById('parcel_dostavka').checked == true) {
            dostavka = 2;
        } else if (document.getElementById('parcel_dostavka').checked == false) {
            dostavka = 0;
        }

        pricePlan = 30;
        if (document.getElementById('parcel_weight').value == '')
        {
            parcel_weight = 1;
//                        document.getElementById('parcel_weight').value = 1;

            if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }
        else
        {
        if (overallWeight > parcel_weight) {
            var price = (overallWeight - parcel_weight) * 2 + parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');

            } else if (overallWeight < parcel_weight) {
            var price = parcel_weight * pricePlan + zabor + dostavka;
//            document.getElementById('parcel_cost').value = Math.round(price);
            document.getElementById('parcel_cost').value = price.toFixed(2).replace(/\.0+$/,'');
            }
        }

    }
}


var selectedRow = null
var sumVall = 0;
function sum(){
var table = document.getElementById("employeeList"), sumVal = 0, costVal=0;
            for(var i = 1; i < table.rows.length; i++)
            {
                sumVal = sumVal + parseInt(table.rows[i].cells[5].innerHTML);
                costVal = costVal + parseInt(table.rows[i].cells[4].innerHTML);
            }
            document.getElementById("parcel_weight").value = sumVal;
            document.getElementById("parcel_total_cost").value = costVal;

            sumVall = sumVal;
            costVal = costVal;
}

function onFormSubmit() {
    if (validate()) {
        var formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }
}
//function filenameget() {
//var tt = $('#prod_images').prop('files')[0];
//alert(tt);
//}
function readFormData() {
    var formData = {};
    formData["prod_name"] = document.getElementById("prod_name").value;
    formData["prod_url"] = document.getElementById("prod_url").value;
    formData["prod_cnt"] = document.getElementById("prod_cnt").value;
    formData["prod_cost"] = document.getElementById("prod_cost").value;
    formData["prod_total_cost"] = parseFloat(document.getElementById("prod_cnt").value) * parseFloat(document.getElementById("prod_cost").value);
    formData["prod_tnved"] = document.getElementById("prod_tnved").value;
    formData["prod_weight"] = document.getElementById("prod_weight").value;

//    formData["prod_images"] = $('#prod_images').prop('files')[0];
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("employeeList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.prod_name;

    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.prod_url;

    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.prod_cnt;

    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.prod_cost;

    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.prod_total_cost;

    cell6 = newRow.insertCell(5);
    cell6.innerHTML = data.prod_tnved;

    cell7 = newRow.insertCell(6);
    cell7.innerHTML = data.prod_weight;

    cell7 = newRow.insertCell(7);
    cell7.innerHTML = `<a href="#" onClick="onEdit(this)">Редактировать</a>
                       <a href="#" onClick="onDelete(this)">Удалить</a>`;
                       calculate();

}

function resetForm() {
    document.getElementById("prod_name").value = "";
    document.getElementById("prod_url").value = "";
    document.getElementById("prod_cnt").value = "";
    document.getElementById("prod_cost").value = "";
    document.getElementById("prod_tnved").value = "";
    document.getElementById("prod_weight").value = "";

    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("prod_name").value = selectedRow.cells[0].innerHTML;
    document.getElementById("prod_url").value = selectedRow.cells[1].innerHTML;
    document.getElementById("prod_cnt").value = selectedRow.cells[2].innerHTML;
    document.getElementById("prod_cost").value = selectedRow.cells[3].innerHTML;
    document.getElementById("prod_tnved").value = selectedRow.cells[5].innerHTML;
    document.getElementById("prod_weight").value = selectedRow.cells[6].innerHTML;

}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.prod_name;
    selectedRow.cells[1].innerHTML = formData.prod_url;
    selectedRow.cells[2].innerHTML = formData.prod_cnt;
    selectedRow.cells[3].innerHTML = formData.prod_cost;
    selectedRow.cells[4].innerHTML = formData.prod_total_cost;
    selectedRow.cells[5].innerHTML = formData.prod_tnved;
    selectedRow.cells[6].innerHTML = formData.prod_weight;
//    selectedRow.cells[6].innerHTML = formData.prod_images;

}

function onDelete(td) {
var table = document.getElementById('employeeList');
    if (confirm('Вы уверены, что хотите удалить эту запись ?')) {
        row = td.parentElement.parentElement;
        var newsum1= parseInt(table.rows[row.rowIndex].cells[5].innerHTML);
        var newsum2= parseInt(table.rows[row.rowIndex].cells[4].innerHTML);
        document.getElementById("employeeList").deleteRow(row.rowIndex);
        var newsum = parseInt(document.getElementById("parcel_weight").value) - newsum1;
        var newsum3 = parseInt(document.getElementById("parcel_total_cost").value) - newsum2;

        if(newsum == 0)
        {
        document.getElementById("parcel_weight").value = '';
        }
        else{
        document.getElementById("parcel_weight").value = newsum;
        }
        if(newsum3 == 0)
        {
           document.getElementById("parcel_total_cost").value = '';
        }
        else
        {
        document.getElementById("parcel_total_cost").value = newsum3;

        }
        calculate();
        resetForm();
    }
}
function validate() {
    isValid = true;
    if (document.getElementById("prod_name").value == "") {
        isValid = false;
        document.getElementById("fullNameValidationError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}



