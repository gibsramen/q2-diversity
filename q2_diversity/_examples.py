# ----------------------------------------------------------------------------
# Copyright (c) 2016-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2


# PD Mice Data
pd_alpha_div_faith_pd_url = ('https://data.qiime2.org/usage-examples/pd-mice/'
                             'core-metrics-results/faith_pd_vector.qza')

pd_metadata_url = (f'https://data.qiime2.org/{qiime2.__release__}/tutorials/'
                   'pd-mice/sample_metadata.tsv')


# Alpha Diversity examples
def alpha_group_significance_faith_pd(use):
    alpha_div_faith_pd = use.init_artifact_from_url('alpha_div_faith_pd',
                                                    pd_alpha_div_faith_pd_url)
    metadata = use.init_metadata_from_url('metadata', pd_metadata_url)

    viz, = use.action(
        use.UsageAction('diversity', 'alpha_group_significance'),
        use.UsageInputs(
            alpha_diversity=alpha_div_faith_pd,
            metadata=metadata
        ),
        use.UsageOutputNames(
            visualization='visualization'
        )
    )

    viz.assert_output_type('Visualization')


def alpha_correlation_faith_pd(use):
    alpha_div_faith_pd = use.init_artifact_from_url('alpha_div_faith_pd',
                                                    pd_alpha_div_faith_pd_url)
    metadata = use.init_metadata_from_url('metadata', pd_metadata_url)

    viz, = use.action(
        use.UsageAction('diversity', 'alpha_correlation'),
        use.UsageInputs(
            alpha_diversity=alpha_div_faith_pd,
            metadata=metadata
        ),
        use.UsageOutputNames(
            visualization='visualization'
        )
    )

    viz.assert_output_type('Visualization')
