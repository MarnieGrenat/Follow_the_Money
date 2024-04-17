from Olympus.Hermes import Hermes

REPETIR_NOS_CRUZAMENTOS = True
DEBUG = False


def save_returns(op: int, path:str, returns:tuple) -> None:
    with open(path[:-4]+'_OUTPUT.txt', 'w') as file:
        file.write(f"Operations: {op}\n\n")
        file.write(f"Amount of Money Collected: {returns[0]}\n\n")
        file.write(f"List of Money Collected: {returns[1]}")

def main(path:str) -> tuple:
    '''
    Main function to execute the program logic.

    Args:
        path (str): The path to the map file.

    Returns:
        tuple: A tuple containing the amount of money collected and a list of money values collected.
    '''
    police = Hermes(path, repeat_value=REPETIR_NOS_CRUZAMENTOS, debug=DEBUG)
    operations = 0
    while (not police.is_at_dead_end()) and (not police.is_not_at_wall()):
        operations+=1
        operations += police.travel_until_curve()
        operations += police.change_curve_direction()

    if DEBUG:
        police.atlas.debug_save(police.direction, operations)

    print(f"Amount of Money Collected: {police.get_money_amount()}")
    print(f"Operations: {operations}")
    save_returns(operations, path, (police.get_money_amount(), police.get_money_list()))

if __name__ == "__main__":
    inputs = [ # lista de casos de teste
        # 'Tests\case-example.txt',
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