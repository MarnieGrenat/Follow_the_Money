from Olympus.Hermes import Hermes

REPETIR_NOS_CRUZAMENTOS = True
DEBUG = False

def save_returns(path:str, returns:tuple) -> None:
    with open(path[:-4]+'_OUTPUT.txt', 'w') as file:
        file.write(f"Amount of Money Collected: {returns[0]}\n\n")
        file.write(f"List of Money Collected: {returns[1]}")

def main(path:str) -> tuple:
    police = Hermes(path, repeat_value=REPETIR_NOS_CRUZAMENTOS, debug=DEBUG)

    while (not police.is_at_dead_end()) and (not police.is_not_at_wall()):
        police.travel_until_curve()
        police.change_curve_direction()

    if DEBUG:
        police.atlas.debug_save(police.direction)

    print(f"Amount of Money Collected: {police.get_money_amount()}")
    save_returns(path, (police.get_money_amount(), police.get_money_list()))


if __name__ == "__main__":
    inputs = [
        # 'Tests\caseG01.txt',
        'Tests\caseG50.txt',
        'Tests\caseG100.txt',
        'Tests\caseG200.txt',
        'Tests\caseG500.txt',
        'Tests\caseG750.txt',
        'Tests\caseG1000.txt',
        'Tests\caseG1500.txt',
        'Tests\caseG2000.txt'
    ]

    for path in inputs:
        print(f"\n[VERBOSE] Initiating Execution!")
        main(path)
        print("[VERBOSE] Execution Finished Successfully!")