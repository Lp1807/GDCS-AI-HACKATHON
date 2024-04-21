#  Egon Sacro Graal



````sql
`SELECT _ingestion_ingester_write_ts, vendor_city, vendor_address, vendor_house_number, vendor_province_abbreviation, vendor_postal_code FROM `skyita-da-daita-prod.account.vendors`order by _ingestion_ingester_write_ts DESC LIMIT 1000 
````



