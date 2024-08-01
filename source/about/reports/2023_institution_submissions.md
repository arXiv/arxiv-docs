
<script type='text/javascript' src="https://code.jquery.com/jquery-3.7.1.js"></script>  
<script type='text/javascript' src="https://cdn.datatables.net/2.1.2/js/dataTables.js"></script>  
<link href="https://cdn.datatables.net/2.1.2/css/dataTables.dataTables.css" rel="stylesheet" type="text/css">  

# Submissions by Institution (2023)

_See more [arXiv in Numbers](2023_usage.md)_

Submissions by Institution will be made available to members only by June 2023. [To learn how this information is used in the membership program, see here](../../about/membership.md). The following table shows submissions by institution in 2021, 2022, and 2023. Don't see your institution? Contact [membership@arxiv.org](mailto:membership.arxiv.org). 


<style>

    .filters-wrapper {
        display: flex;
        flex-direction: row;
        margin-bottom: 20px;
    }

    /* Clear floats after the columns */
    .filters-wrapper:after {
    content: "";
    display: table;
    clear: both;
    }

    .filters-container {
        max-height: 200px;
        overflow-y: auto;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: .9em;
        float: left;
    }

    .filter-item {
        margin-right: 20px;
        width: 50%;
    }

    table.dataTable {
        margin: 0 auto;
        font-size: .9em; 
    }

    table.dataTable thead th {
        white-space: nowrap;
    }

</style>

<div class="filters-wrapper">
    <div class="filter-item">
        <h4>Institution Name</h4> 
        <div class="filters-container" id="institution-filter-container">
            <div id="institution-filter"></div>
        </div>
    </div>
    <div class="filter-item">
        <h4>Country</h4>
        <div class="filters-container" id="country-filter-container">
            <div id="country-filter"></div>
        </div>
    </div>
</div>

<div id="institution_rank_wrapper" style="max-width: 1200px;">
    <table id="institution_rank" class="display compact"></table>
</div>


<script type='text/javascript' src="https://storage.googleapis.com/info-arxiv-org-stats/institution_submissions_top_filter_v10.js"></script>

Data provided by
<img width="44" style="vertical-align:middle" src='https://arxiv.org/scopus.png'/>  

