'''
Created on 2023/10/13

@author: t21cs060
'''
import random

# じゃんけんの手を定義
hands = ["グー", "チョキ", "パー"]

# プレイヤー数を指定
num_players = int(input("プレイヤーの数を入力してください（3人以上）: ")

# じゃんけんの試合数を指定
num_games = 3

# プレイヤーごとに勝ち点を記録する辞書を作成
scores = {i: 0 for i in range(num_players)}

# じゃんけんのメインループ
for game in range(num_games):
    print(f"\n第{game + 1}試合:")
    
    # 各プレイヤーの手をランダムに選択
    round_choices = {i: random.randint(0, 2) for i in range(num_players)}
    
    # 選択した手を表示
    for player, choice in round_choices.items():
        print(f"プレイヤー{player + 1}の選択: {hands[choice]}")
    
    # 勝者を判定し、勝ち点を記録
    winning_hand = max(round_choices.values(), key=round_choices.values().count)
    for player, choice in round_choices.items():
        if choice == winning_hand:
            scores[player] += 1

# 勝者を決定
winning_score = max(scores.values())
winners = [player + 1 for player, score in scores.items() if score == winning_score]

if len(winners) == 1:
    print(f"\nプレイヤー{winners[0]}が{winning_score}試合中{num_games}試合で勝利しました!")
else:
    print("\n引き分けです。")

# 勝者とスコアを表示
print("\n最終スコア:")
for player, score in scores.items():
    print(f"プレイヤー{player + 1}: {score}勝")