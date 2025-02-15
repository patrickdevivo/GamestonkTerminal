""" opensea.io View """

import logging
import os

from gamestonk_terminal.cryptocurrency.nft.opensea_model import get_collection_stats
from gamestonk_terminal.decorators import log_start_end
from gamestonk_terminal.helper_funcs import export_data, print_rich_table
from gamestonk_terminal.rich_config import console

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def display_collection_stats(slug: str, export: str):
    """Display collection stats. [Source: opensea.io]

    Parameters
    ----------
    slug: str
        Opensea collection slug.
        If the name of the collection is Mutant Ape Yacht Club the slug is mutant-ape-yacht-club
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    collection_stats_df = get_collection_stats(slug)
    if collection_stats_df.empty:
        console.print("No data found.", "\n")
    else:
        print_rich_table(
            collection_stats_df,
            headers=list(collection_stats_df.columns),
            show_index=False,
            title="Collection Stats",
        )
        console.print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "stats",
        collection_stats_df,
    )
