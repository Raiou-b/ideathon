# randomモジュールをインポート（ランダムな選択を行うため）
import random

# アイデア生成クラスの定義
class IdeathonIdeaGenerator:
    """
    アイデアソンのためのランダムアイデア生成ツール。
    アイデア、制約条件、検討すべき質問をランダムに組み合わせて出力します。
    """
    
    def __init__(self):
        """クラスの初期化メソッド。アイデア、制約、質問のリストを初期化します。"""
        # アイデアのリスト（アイデアソンのテーマ候補）
        self.ideas = [
            "Eco-friendly product",              # エコフレンドリー製品
            "AI-based health solution",          # AI技術を用いた健康ソリューション
            "Remote team collaboration tool",    # リモートチーム協働ツール
            "Virtual reality education platform", # VR教育プラットフォーム
            "Sustainable fashion brand"          # サステナブルファッションブランド
        ]
        
        # 制約条件のリスト（プロジェクト実行時の条件）
        self.constraints = [
            "Budget under $5000",                           # 予算5000ドル以下
            "Must use renewable resources",                 # 再生可能資源の使用必須
            "Team must consist of at least 3 members",      # 最低3人以上のチーム構成
            "Must have a social impact",                    # 社会的インパクトが必要
            "Should be applicable in developing countries"  # 発展途上国での適用可能性
        ]
        
        # 検討すべき質問のリスト（アイデア評価の指標）
        self.questions = [
            "How will this idea create value?",             # このアイデアはどのような価値を生み出すか？
            "Who is the target audience?",                  # ターゲットオーディエンスは誰か？
            "What are the potential challenges?",           # 潜在的な課題は何か？
            "How can this idea be implemented effectively?", # このアイデアはどう効果的に実装できるか？
            "What resources are needed?"                    # どのようなリソースが必要か？
        ]

    def generate_idea(self):
        """
        ランダムにアイデア、制約条件、質問を選択して組み合わせます。
        
        Returns:
            dict: 以下のキーを持つ辞書
                - idea: ランダムに選択されたアイデア
                - constraint: ランダムに選択された制約条件
                - question: ランダムに選択された質問
        """
        # 各リストからランダムに1つずつ選択
        idea = random.choice(self.ideas)          # ランダムなアイデア
        constraint = random.choice(self.constraints)  # ランダムな制約条件
        question = random.choice(self.questions)  # ランダムな質問
        
        # 選択された3つの要素を辞書形式で返す
        return {
            "idea": idea,
            "constraint": constraint,
            "question": question
        }

# スクリプトが直接実行された場合に実行するメイン処理
if __name__ == '__main__':
    # ジェネレータのインスタンスを作成
    generator = IdeathonIdeaGenerator()
    
    # ランダムなアイデアを生成
    result = generator.generate_idea()
    
    # 生成されたアイデアを表示
    print(result)