from .Police import Police
from .Map import Map

def main(path:str) -> tuple:
    police = Police(Map(path))

    while (police.position not in police.map.end_or_wall):
        police.travel_until_curve()
        police.position = police.change_direction()

    return (police.money_bag.get_amount(), police.money_bag.get_money_list())




if __name__ == "__main__":
    print(f"[VERBOSE] Initiating Executed!")
    main('./test-cases/casoG50.txt')
    print("[VERBOSE] Execution Finished Successfully!")