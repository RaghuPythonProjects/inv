base_folder = 'inventory_reports'  # master folder to store all files

max_sheet_rows = 1048000

report_api_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json;charset=UTF-8',
            'Authorization': 'Basic bnhhZG1pbjpjMGNmYTRjNDg3NWM3N2E4NTY1MjdhOWMwZmI5YjUzZg=='
        }

his_config = {

    # required
    # report name / folder
    'report_name': 'HIS',

    # required
    'severity': 7.0,

    # required
    "paths": {
        "raw_data_folder": "RawData",  # required
        "processed_data_folder": "ProcessedData",  # required
        "merge_data_folder": "MergedData"  # optional and can set as None
    },

    # Required
    # reportID : FileName,
    "report_dict": {
        33827: 'GJDE - OS',
        33828: 'GJDE - Application',
        34335: 'eLog - OS',
        34336: 'eLog - Application',
        34337: 'EDS - OS',
        34338: 'EDS - Application',
        33829: 'Windchill - OS',
        33830: 'Windchill - Application'
    },

    # optional
    # files_set : [file1, file2, file x], master_file_name: file name to save master file
    "merge_files_dict": [
        {'files_set': ['GJDE - OS', 'GJDE - Application'], 'master_file_name': 'GJDE - Vulnerabilities'},
        {'files_set': ['eLog - OS', 'eLog - Application'], 'master_file_name': 'eLog - Vulnerabilities'},
        {'files_set': ['EDS - OS', 'EDS - Application'], 'master_file_name': 'EDS - Vulnerabilities'},
        {'files_set': ['Windchill - OS', 'Windchill - Application'], 'master_file_name': 'Windchill - Vulnerabilities'},
    ],

    # optional
    # [sheet name 1, sheet name 2, sheet name x] for each file in file_set in merge_files_dict
    "merge_files_sheets": ['OS', 'APP'],

    # optional
    # sharepoint folder path to upload files to
    # uploaded to latest_folder_path \ latest_folder_name
    'latest_folder_path': 'Shared Documents/Weekly Reporting/!LATEST-Weekly-Reports',
    'latest_folder_name': "!LATEST-HIS-Inventory-Reports",

    # optional
    # sharepoint folder path to upload files to
    # uploaded to history_folder_path \ year \ week date \ history_folder_name
    'history_folder_path': 'Shared Documents/Weekly Reporting',
    'history_folder_name': 'High Impact System',

}

workstations_config = {

    # required
    # report name / folder
    'report_name': 'Workstations',

    # required
    'severity': 7.0,

    # required
    "paths": {
        "raw_data_folder": "RawData",  # required
        "processed_data_folder": "ProcessedData",  # required
        "merge_data_folder": "MergedData"  # optional and can set as None
    },

    # Required
    # reportID : FileName,
    "report_dict": {
        33587: "LTI Workstations - OS",
        33589: "LTI Workstations - Applications",
        33588: "Atos Workstations - OS",
        33586: "Atos Workstations - Applications",
    },

    # optional
    # files_set : [file1, file2, file x], master_file_name: file name to save master file
    "merge_files_dict": [],

    # optional
    # [sheet name 1, sheet name 2, sheet name x] for each file in file_set in merge_files_dict
    "merge_files_sheets": [],

    # optional
    # sharepoint folder path to upload files to
    # uploaded to latest_folder_path \ latest_folder_name
    'latest_folder_path': 'Shared Documents/Weekly Reporting/!LATEST-Weekly-Reports',
    'latest_folder_name': "!LATEST-Workstation-Reports",

    # optional
    # sharepoint folder path to upload files to
    # uploaded to history_folder_path \ year \ week date \ history_folder_name
    'history_folder_path': 'Shared Documents/Weekly Reporting',
    'history_folder_name': "Workstation Reports",

}

standard_config = {

    # required
    # report name / folder
    'report_name': 'Standard',

    # required
    'severity': 7.0,

    # required
    "paths": {
        "raw_data_folder": "RawData",  # required
        "processed_data_folder": "ProcessedData",  # required
        "merge_data_folder": "MergedData"  # optional and can set as None
    },

    # Required
    # reportID : FileName,
    "report_dict": {
        33492: "APAC - OS",
        33493: "AMER - OS",
        33248: "APAC - Applications",
        33488: "AMER - Applications",
        33494: "EMEA - OS",
        33487: "EMEA - Applications",
        33378: "CGI - OS",
        33484: "CGI - Applications",
        33295: "Synology",
        33243: "AMER - Network",
        33242: "EMEA - Network",
        33241: "APAC - Network",
        33274: "UC",
        33582: "DXC - OS",
        33583: "DXC - Applications",
        33256: "DXC"
    },

    # optional
    # files_set : [file1, file2, file x], master_file_name: file name to save master file
    "merge_files_dict": [],

    # optional
    # [sheet name 1, sheet name 2, sheet name x] for each file in file_set in merge_files_dict
    "merge_files_sheets": [],

    # optional
    # sharepoint folder path to upload files to
    # uploaded to latest_folder_path \ latest_folder_name
    'latest_folder_path': 'Shared Documents/Weekly Reporting/!LATEST-Weekly-Reports',
    'latest_folder_name': "!LATEST-Standard-Reports",

    # optional
    # sharepoint folder path to upload files to
    # uploaded to history_folder_path \ year \ week date \ history_folder_name
    'history_folder_path': 'Shared Documents/Weekly Reporting',
    'history_folder_name': "Standard Reports",

}

