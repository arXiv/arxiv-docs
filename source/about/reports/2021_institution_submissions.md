<script type='text/javascript' src="https://code.jquery.com/jquery-3.7.1.js"></script>  
<script type='text/javascript' src="https://cdn.datatables.net/2.1.2/js/dataTables.js"></script>  
<link href="https://cdn.datatables.net/2.1.2/css/dataTables.dataTables.css" rel="stylesheet" type="text/css"> 

# Submissions by Institution (2021)

_See more [arXiv in Numbers](2021_usage.md)_

Submissions by Institution will be made available to members only by June 2022.

The following table shows submissions by institution in 2019, 2020, and 2021. To search for a specific institution, hover your mouse over the right hand corner of the list of institutions to reveal the search icon. [To learn how this information is used in the membership program, see here](../../about/membership.md).



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

<div class="filters-wrapper">
    <div class="filter-item">
        <h4 style="margin-bottom: 0px;">Institution Name</h4>
        <input type="text" id="institution-search" placeholder="Search institutions...">
        <div class="filters-container" id="institution-filter-container">
            <div id="institution-filter"></div>
        </div>
    </div>
    <div class="filter-item">
        <h4 style="margin-bottom: 0px;">Country</h4>
        <input type="text" id="country-search" placeholder="Search countries...">
        <div class="filters-container" id="country-filter-container">
            <div id="country-filter"></div>
        </div>
    </div>
</div>

<div id="institution_rank_wrapper">
    <table id="institution_rank" class="display compact"></table>
</div>


<script type='text/javascript' src="https://storage.googleapis.com/info-arxiv-org-stats/2021_institution_submissions.js"></script>

Data provided by
<img width="44" style="vertical-align:middle" src='https://arxiv.org/scopus.png'/>
