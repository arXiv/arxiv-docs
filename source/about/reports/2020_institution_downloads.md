---
hide:
- toc
---

<script type='text/javascript' src="https://code.jquery.com/jquery-3.7.1.js"></script>  
<script type='text/javascript' src="https://cdn.datatables.net/2.1.2/js/dataTables.js"></script>  
<link href="https://cdn.datatables.net/2.1.2/css/dataTables.dataTables.css" rel="stylesheet" type="text/css"> 

# Downloads by Institution in 2020

_See more [arXiv in Numbers](2020_usage.md)_

The following table shows institutions' downloads for 2020. 

**Note**: Please see caveats related to usage data on [arXiv in Numbers](2020_usage.md)

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

    #domain_rank_wrapper {
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

    #domain-filter br,
    #year-filter br {
        display: none;
    }

    #domain-filter label,
    #year-filter label {
        display: flex;
        align-items: flex-start;
        margin-bottom: 5px;
        line-height: 1.2;
    }

    #domain-filter input[type="checkbox"],
    #year-filter input[type="checkbox"] {
        margin-right: 5px;
        margin-top: 2px;
    }

    #domain-filter label span,
    #year-filter label span {
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
        <h4 style="margin-bottom: 0px;">Domain</h4>
        <input type="text" id="domain-search" placeholder="Search domains...">
        <div class="filters-container" id="domain-filter-container">
            <div id="domain-filter"></div>
        </div>
    </div>
</div>

<div id="domain_rank_wrapper">
    <table id="domain_rank" class="display compact"></table>
</div>


<script type='text/javascript' src="https://storage.googleapis.com/info-arxiv-org-stats/2020_downloads_by_institution.js"></script>
