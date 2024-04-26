from utilities.vulnerability_report_processor import VulnerabilityReportProcessor
from utilities.inventory_files_config import his_config, workstations_config


def main():
    auto_manager = VulnerabilityReportProcessor(config=his_config, download_new_reports=True)
    auto_manager.run()

    auto_manager = VulnerabilityReportProcessor(config=workstations_config, download_new_reports=True)
    auto_manager.run()


if __name__ == "__main__":
    main()