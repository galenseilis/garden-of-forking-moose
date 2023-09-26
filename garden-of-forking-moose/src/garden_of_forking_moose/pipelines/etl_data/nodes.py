"""
This is a boilerplate pipeline 'etl_data'
generated using Kedro 0.18.13
"""
import pyinaturalist

def get_inat_data() -> dict:
    '''Fetches response from iNat API to get moose data.

    Returns
    -------
    response: dict
        Response from iNaturalist to obtain moose data.
    '''
    session = pyinaturalist.ClientSession(per_minute=50)

    response = pyinaturalist.get_observations(
                taxon_id=522193, # Must be Alces alces
                quality_grade='research', # Must be research grade observation
                geo=True, # Must have geolocation
                geoprivacy='open', # Must have open geoprivacy settings
                term_id=22, # Evidence of presence
                term_value_id=24, # Organism
                page='all', # Get all data
                session=session # Rate-limited session
                )

    return response
