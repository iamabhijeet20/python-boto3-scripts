import pygsheets
import pandas as pd
import ec2details

# Authenticate and open the Google Sheet
def open_google_sheet(credentials_file, sheet_title, worksheet_title):
    gc = pygsheets.authorize(service_file=credentials_file)
    sheet = gc.open(sheet_title)
    worksheet = sheet.worksheet_by_title(worksheet_title)
    return worksheet

# Read data from a worksheet
def read_worksheet(worksheet):
    return worksheet.get_as_df()

# Find the next empty row in a specific column (e.g., column A)
def find_next_empty_row(worksheet, col=1):
    values = worksheet.get_col(col, include_tailing_empty=False)
    return len(values) + 1  # Return the index of the next empty row

# Check if data already exists in the worksheet
def check_data_exists(worksheet, data):
    all_data = worksheet.get_all_records()
    for row in all_data:
        if row['Instance Name'] == data[0] and row['Instance Id '] == data[1]:
            return True
    return False

# Write data to the next available row if it doesn't already exist
def write_to_next_row_if_not_exists(worksheet, data):
    if not check_data_exists(worksheet, data):
        next_row = find_next_empty_row(worksheet)
        worksheet.update_row(next_row, data)
    else:
        print(f"Data already exists: {data}")

# Example usage:
if __name__ == "__main__":
    # Replace with your own credentials JSON file
    credentials_file = 'creds.json'
    
    sheet_title = 'Ec2-instances'
    worksheet_title = 'Sheet1'
    
    worksheet = open_google_sheet(credentials_file, sheet_title, worksheet_title)

    # Example: Write data to the next available row if not exists
    data_to_write = [ec2details.tag_name, ec2details.instance_id, ec2details.instance_type, 
                     ec2details.AvailabilityZone, ec2details.PublicIp, ec2details.KeyName, 
                     ec2details.GroupId, ec2details.GroupName, ec2details.VpcId]

    # Write the data to the next available row if it doesn't already exist
    write_to_next_row_if_not_exists(worksheet, data_to_write)
    
    worksheet.sync()
