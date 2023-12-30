from dataclasses import dataclass

# Data ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    #this clas will return be entities;
    imbalance_data_file_path: str
    raw_data_file_path: str