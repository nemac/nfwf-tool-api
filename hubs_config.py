from collections import OrderedDict

config = {
  'continental_us': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'hub_rnk': 'int',
        'wildlife': 'float',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'aquatic': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'drainage': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'geostress': 'float',
        'slr': 'float',
        'slope': 'float',
        'stormsurge': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'storm_surge': 'stormsurge'
    },
  },

  'us_virgin_islands': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'stormsurge': 'float',
        'impermeabl': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'wildlife': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'storm_surge': 'stormsurge',
      'impermeable': 'impermeabl',
      'rank_val': 'hub_rnk'
    }
  },

  'puerto_rico': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'stormsurge': 'float',
        'impermeabl': 'float',
        'landslides': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'tsunami': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'storm_surge': 'stormsurge',
      'impermeable': 'impermeabl',
      'rank_val': 'hub_rnk'
    }
  },

  'northern_mariana_islands': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'impermeabl': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'wave_flood': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'impermeable': 'impermeabl',
      'wave_flooding': 'wave_flood',
      'rank_val': 'hub_rnk'
    }
  },

  'hawaii': {
    'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'impermeabl': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'tsunami': 'float',
        'landslides': 'float',
        'stormsurge': 'float'
      }
    }),
    'field_maps': {
      'storm_surge': 'stormsurge',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'impermeable': 'impermeabl',
      'hub_rank': 'hub_rnk'
    }
  }


}
