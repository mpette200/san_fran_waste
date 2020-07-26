## Machine Learning - Garbage Cleaning in San Francisco

This project attempts to apply machine learning to a data set containing details collected when garbage receptacles have been reported as overflowing. The data is publicly available from (https://datasf.org).

Possible business cases might be:
- Is it possible to predict locations and times when receptacles get full? This could help in assigning crews.
- Some reports turn out to be false, might be useful if this could be predicted.
- Do weather conditions have any effect? (Extra project to compare with weather data)


## Columns in the Data Set
Description of the columns in the data set is in the table below. Basic exploratory data analysis (EDA) using Sweetviz can be found in (https://mpette200.github.io/san_fran_waste/sweetviz/SWEETVIZ_REPORT.html).


|    | Column Name         | Description                                                                                                                                                       | Type        |
|---:|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
|  0 | CaseID              | The unique ID of the service request created.                                                                                                                     | Number      |
|  1 | Opened              | The date and time when the service request was made                                                                                                               | Date & Time |
|  2 | Closed              | The date and time when the service request was closed                                                                                                             | Date & Time |
|  3 | Updated             | The date and time when the service request was last modified. For requests with status=closed, this will be the date the request was closed                       | Date & Time |
|  4 | Status              | A single-word indicator of the current state of the service request. (Note: GeoReport V2 only permits ‘open’ and ‘closed’)                                        | Plain Text  |
|  5 | Status Notes        | Explanation of why status was changed to current state or more details on current status than conveyed with status alone                                          | Plain Text  |
|  6 | Responsible Agency  | The agency responsible for fulfilling or otherwise addressing the service request.                                                                                | Plain Text  |
|  7 | Category            | The human readable name of the service request type                                                                                                               | Plain Text  |
|  8 | Request Type        | The human readable name of the service request subtype                                                                                                            | Plain Text  |
|  9 | Request Details     | The human readable name of the service request details                                                                                                            | Plain Text  |
| 10 | Address             | Human readable address or description of location                                                                                                                 | Plain Text  |
| 11 | Street              | Primary Street of the associated address. Parks may have a park name instead of a street name. Requests not associated with an address will be blank.             | Plain Text  |
| 12 | Supervisor District | San Francisco Supervisor District as defined in 'Supervisor Districts as of April 2012'                                                                           | Number      |
| 13 | Neighborhood        | San Francisco Neighborhood as defined in 'SF Find Neighborhoods'                                                                                                  | Plain Text  |
| 14 | Police District     | San Francisco Police District as defined in 'Current Police Districts'                                                                                            | Plain Text  |
| 15 | Latitude            | Latitude of the location, using the WGS84 projection                                                                                                              | Number      |
| 16 | Longitude           | Longitude of the location, using the WGS84 projection                                                                                                             | Number      |
| 17 | Point               | Combination of Latitude and Longitude for Socrata native maps                                                                                                     | Location    |
| 18 | Source              | Mechanism or path by which the service request was received; typically ‘Phone’, ‘Text/SMS’, ‘Website’, ‘Mobile App’, ‘Twitter’, etc but terms may vary by system. | Plain Text  |
| 19 | Media URL           | A URL to media associated with the request, e.g. an image.                                                                                                        | Website URL |