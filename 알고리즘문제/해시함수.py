import hashlib
import json


class Block():
    def __init__(self, data):  # Block 객체가 생성될 때 초기화
        self.nounce = 0
        self.data = data
        self.prevhash = ""
        self.hash = self.calHash()

    def calHash(self):  # 현재 블록의 해쉬 값 생성
        return hashlib.sha256(str(self.nounce).encode() + str(self.data).encode() +
                              str(self.prevhash).encode()).hexdigest()

    def mine(self, difficulty):
        ans = ["0"] * difficulty
        answer = "".join(ans)
        while (str(self.hash)[:difficulty] != answer):
            self.nounce += 1
            self.hash = self.calHash()
        return self.hash


class BlockChain:
    def __init__(self, ):
        self.chain = []
        self.difficulty = 5  # 0의 갯수
        self.createGenesis()

    def createGenesis(self):  # 최초 블럭 생성
        self.chain.append(Block('Genesis Block'))

    def addBlock(self, nBlock):  # 블록을 체인에 추가
        nBlock.prevhash = self.chain[len(self.chain) - 1].hash
        nBlock.hash = nBlock.mine(self.difficulty)
        self.chain.append(nBlock)

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def isValid(self):  # 체인 유효성검사
        i = 1
        while (i < len(self.chain)):
            if (self.chain[i].hash != self.chain[i].calHash()):  # 현재 블록의 해쉬 값,  계산된 해쉬 값 비교
                return False
            if (self.chain[i].prevhash != self.chain[i - 1].hash):  # 현재 이전 블록의 해쉬 값과 이전 블록에 저장되어 있는 해쉬 값 비교
                return False
            i += 1
        return True


mychain = BlockChain()
mychain.addBlock(Block("2nd"))
mychain.addBlock(Block("3rd"))
for block in mychain.chain:
    print(json.dumps(vars(block), indent=4))