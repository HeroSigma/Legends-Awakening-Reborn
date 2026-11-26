"""Signature partners shared by roster authoring and story audits."""
def align_ace(key, team):
    ace = None
    if key.startswith('TRAINER_BRENDAN_ROUTE_'): ace = 'SWAMPERT'
    elif key.startswith('TRAINER_MAY_ROUTE_'): ace = 'BLAZIKEN'
    elif key == 'TRAINER_WALLY_MAUVILLE': ace = 'KIRLIA'
    elif key.startswith('TRAINER_WALLY_VR_'): ace = 'GALLADE'
    elif key == 'TRAINER_RED': ace = 'PIKACHU'
    elif key == 'TRAINER_LEAF': ace = 'BLASTOISE'
    elif key == 'TRAINER_SILVER_RUSTBORO': ace = 'FERALIGATR'
    elif key == 'TRAINER_BARRY_ROUTE_110':
        team = ['FLOATZEL' if sp == 'RAPIDASH' else sp for sp in team]
        ace = 'INFERNAPE'
    team = list(team)
    if ace:
        if ace in team: team.remove(ace)
        else: team.pop()
        team.append(ace)
    return team
