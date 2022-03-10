class DataDto:
    def __init__(self, cluster_name, cluster_id, scholarly_output, publication_share, fwci, prominence_percentile):
        self.cluster_name = cluster_name
        self.cluster_id = cluster_id
        self.scholarly_output = scholarly_output.replace(",", "")
        self.publication_share = publication_share
        self.fwci = fwci
        self.prominence_percentile = prominence_percentile
