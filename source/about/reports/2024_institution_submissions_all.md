<meta charset="UTF-8">
<!--
<script type='text/javascript' src="https://code.jquery.com/jquery-3.7.1.js"></script>  
<script type='text/javascript' src="https://cdn.datatables.net/2.1.2/js/dataTables.js"></script>  
<link href="https://cdn.datatables.net/2.1.2/css/dataTables.dataTables.css" rel="stylesheet" type="text/css">  
-->
<script type='text/javascript' src="https://code.jquery.com/jquery-3.7.1.js"></script>  
<script type='text/javascript' src="https://cdn.datatables.net/2.3.2/js/dataTables.min.js"></script>  
<link href="https://cdn.datatables.net/2.3.2/css/dataTables.dataTables.css" rel="stylesheet" type="text/css">  

# Submissions by Institution (2024)

_See more [arXiv submission statistics](https://arxiv.org/stats/main)._

Institutional members can view annual reports on their membership dashboard. [To learn how this information is used in the membership program, see here](../../about/membership.md). The following table shows submissions by institution in 2022, 2023, and 2024. Don't see your institution? Contact [membership@arxiv.org](mailto:membership.arxiv.org). 

---
**NOTE**

  - Please allow 20-30 seconds for the table to fully load. The filter UI may be unresponsive until the data is fully loaded. 
  - The filter options are combined with a <strong>logical AND</strong>. In general, you will want to Select All on at least one column.

---


<style>

    .filters-wrapper {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        width: 100%;
    }

    .filter-item {
        box-sizing: border-box;
    }

    .filter-item:first-child {
        width: calc(65% - 20px);
    }

    .filter-item:last-child {
        width: 35%;
    }

.filters-container {
    height: 200px;
    overflow-y: auto;
    border: 1px solid #ccc;
    padding: 10px;
    font-size: .9em;
}

    #institution_rank_wrapper {
        width: 100%;
    }

    .dataTables_wrapper {
        width: 100%;
    }

    .dataTables_filter {
        width: 30%;
        float: right;
    }

    table.dataTable {
        width: 100% !important;
        font-size: .9em; 
    }

    table.dataTable thead th {
        white-space: nowrap;
    }

    #institution-filter br,
    #country-filter br {
        display: none;
    }

    #institution-filter label,
    #country-filter label {
        display: flex;
        align-items: flex-start;
        margin-bottom: 5px;
        line-height: 1.2;
    }

    #institution-filter input[type="checkbox"],
    #country-filter input[type="checkbox"] {
        margin-right: 5px;
        margin-top: 2px;
    }

    #institution-filter label span,
    #country-filter label span {
        display: inline-block;
        padding-left: 20px;
        text-indent: -20px;
    }

    .filter-item input[type="text"] {
        width: 100%;
        padding: 5px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
</style>


<h4 style="margin: 0;">Filter Options</h4>
<div class="filters-wrapper">    
    <div class="filter-item">
        <h5 style="margin-bottom: 0px;">Institution Name</h5>
        <input type="text" id="institution-search" placeholder="Filter institution selector">
        <div class="filters-container" id="institution-filter-container">
            <div id="institution-filter"></div>
        </div>
    </div>
    <div class="filter-item">
        <h5 style="margin-bottom: 0px;">Country</h5>
        <input type="text" id="country-search" placeholder="Filter country selector">
        <div class="filters-container" id="country-filter-container">
            <div id="country-filter"></div>
        </div>
    </div>
</div>
<p>
</p>

<hr style="margin: 1em 0;"> 

<div id="institution_rank_wrapper">
    <h4>Announced Submissions by Institution</h4>
    <table id="institution_rank" class="display compact"></table>
</div>


<script type='text/javascript' src="https://storage.googleapis.com/info-arxiv-org-stats/institution_submissions_2024_all.js"></script>

<script type='text/javascript'>
    let institutions = [];
let countries = [];

let selectedInstitutions = [];
let selectedCountries = [];

// console.log(dataSet)
dataSet.forEach(entry => {
	const institution = entry[1];
	const country = entry[3];
	institutions.push(institution);
	countries.push(country);
});

// console.log(institutions)
// console.log(countries)


jQuery.fn.dataTable.ext.type.order['ignore-punct-pre'] = function(data) {
  // Remove leading punctuation and whitespace
  return data.replace(/^[\p{P}\p{S}\s]+/u, '').toLowerCase();
};


//function reorderFilter(list) {
//	return [...new Set(list)].sort();
//}
function reorderFilter(list) {
    return [...new Set(list)].sort((a, b) => {
        const stripPunctuation = str => str.replace(/^[^\w\s]+/, '').toLowerCase();
        return stripPunctuation(a).localeCompare(stripPunctuation(b));
    });
}


institutions = reorderFilter(institutions)
countries = reorderFilter(countries)

function createFilterOptions(containerId, items, selectedItems) {
	const container = document.getElementById(containerId);

	if (!container) {
		console.error(`Container with ID '${containerId}' not found`);
		return;
	}
	const selectAllLabel = document.createElement('label');
	selectAllLabel.htmlFor = `${containerId}-select-all`;

	const selectAllCheckbox = document.createElement('input');
	selectAllCheckbox.type = 'checkbox';
	selectAllCheckbox.id = `${containerId}-select-all`;
	selectAllCheckbox.value = 'select-all';
	selectAllCheckbox.checked = true;

	selectAllLabel.appendChild(selectAllCheckbox);
	selectAllLabel.appendChild(document.createTextNode('Select/Deselect All'));

	container.appendChild(selectAllLabel);
	container.appendChild(document.createElement('br'));

	selectAllCheckbox.addEventListener('change', function() {
		const checkboxes = container.querySelectorAll(`input[type=checkbox]:not(#${containerId}-select-all)`);
		checkboxes.forEach(checkbox => {
			checkbox.checked = this.checked;
			const itemIndex = selectedItems.indexOf(checkbox.value);
			if (this.checked && itemIndex === -1) {
				selectedItems.push(checkbox.value);
			} else if (!this.checked && itemIndex > -1) {
				selectedItems.splice(itemIndex, 1);
			}
		});
		updateTable();
	});

	items.forEach((item,index) => {
		const label = document.createElement('label');
		label.htmlFor=`${containerId}-checkbox-${index}`;

		const checkbox = document.createElement('input');
		checkbox.type = 'checkbox';
		checkbox.id = `${containerId}-checkbox-${index}`;
		checkbox.value = item;
		checkbox.checked = true;

		selectedItems.push(item);

		label.appendChild(checkbox);
		label.appendChild(document.createTextNode(item));

		container.appendChild(label);
		container.appendChild(document.createElement('br'));
	});

	updateTable(); 

	container.addEventListener('change', (event) => {
		if (event.target.type === 'checkbox') {
			if (event.target.checked) {
				selectedItems.push(event.target.value);
			} else {
				const index = selectedItems.indexOf(event.target.value);
				if (index > -1) {
					selectedItems.splice(index, 1);
				}
			}
			const allChecked = Array.from(container.querySelectorAll(`input[type=checkbox]:not(#${containerId}-select-all)`)).every(cb => cb.checked);
			selectAllCheckbox.checked = allChecked;
			updateTable();
		}
	});
}

const escapeRegex = str => str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function updateTable() {
	var institutionRegex = new RegExp(
        `^(?:${selectedInstitutions.map(escapeRegex).join('|')})$`,
        'u' // unicode aware
    );
    // This does not work with dashes:
    // var institutionRegex = new RegExp(
    //     `^(?:${selectedInstitutions.map(name => $.fn.dataTable.util.escapeRegex(name)).join('|')})$`,
    //     'u' // unicode aware
    // );
    //console.log(institutionRegex);
    //console.log(institutionRegex.test("CNRS Ingénierie")); // true
	var countryRegex = `^(${selectedCountries.join('|')})$`;
	table.column(1).search(institutionRegex.source, true, false);
	table.column(3).search(countryRegex, true, false);
	table.draw();
}

let table;

$(document).ready(function () {
    // Initialize data table
    table = $('#institution_rank').DataTable({
        data: dataSet, // This should be an array of arrays or array of objects
        columns: [
            { title: 'Rank' },
            { title: 'Org Name' },
            { title: 'ROR.org' },
            { title: 'Org Country' },
            { title: 'Avg Papers' }
        ],
        columnDefs: [{ type: 'string-utf8', targets: 1 }],
        pageLength: 25
    });

    // Filter institutions
	$("#institution-search").on("keyup", function () {
        const value = $(this).val().toLowerCase();
        $("#institution-filter label").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    // Filter country
	$("#country-search").on("keyup", function () {
		const value = $(this).val().toLowerCase();
		$("#country-filter label").filter(function () {
			$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
		});
	});

    createFilterOptions('institution-filter',institutions,selectedInstitutions);
    createFilterOptions('country-filter',countries,selectedCountries);
});

</script>


2022 and 2023 data provided by
<img width="44" style="vertical-align:middle" src='https://arxiv.org/scopus.png'/>