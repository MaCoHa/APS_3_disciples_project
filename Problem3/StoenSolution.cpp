#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <unordered_map>

using namespace std;

struct RainInfo
{
    long year, rainfall, index;
    RainInfo(long y = 0, long r = 0, long i = 0): year(y), rainfall(r), index(i) {}

    bool operator<(const RainInfo &other) const {
        return year < other.year;
    }
};

class SegmentTree
{
    vector<RainInfo> infos;

    struct Node {
        long startIndx, endIndx, maxRain;
        Node *left, *right;

        Node(long s, long e, long m, Node *l, Node *r)
            : startIndx(s), endIndx(e), maxRain(m), left(l), right(r) {}

        ~Node() {
            delete left;
            delete right;
        }
    };

    Node *root = nullptr;

public:
    SegmentTree(const vector<RainInfo> &infos){
        init(infos);
    }

    ~SegmentTree() {
        delete root;
    }

    long query(long startY, long endY){
        return query(root, startY, endY);
    }

private:
    void init(const vector<RainInfo> &fs){
        delete root;
        infos = fs;
        root = makeTree(0, infos.size() - 1);
    }

    Node* makeTree(int start, int end){
        if (start == end){
            Node *n = new Node(start, end, infos.at(start).rainfall, nullptr, nullptr);
            return n;
        }

        assert(end > start);

        int m = (start + end)/2;
        Node *l = makeTree(start, m);
        Node *r = makeTree(m + 1, end);

        long maxRain = std::max(l->maxRain, r->maxRain);
        Node *n = new Node(start, end, maxRain, l, r);
        return n;
    }

    long query(Node *n, long startY, long endY)
    {
        if (!n) 
            return -1;

        long nStartY = infos.at(n->startIndx).year;
        long nEndY = infos.at(n->endIndx).year;
        if (endY < nStartY || startY > nEndY)
            return -1;

        if (startY <= nStartY && nEndY <= endY)
            return n->maxRain;

        long leftMax = query(n->left, startY, endY);
        long rightMax = query(n->right, startY, endY);
        return std::max(leftMax, rightMax);
    }
};

//#define num(x) (#x".") 
#define num(x) ""

int
main()
{
    bool first = true;
    int m, n;
    while(true){
        cin >> m;
        if (m == 0)
            break;

        unordered_map<long, RainInfo> rainfallsHash;
        vector<RainInfo> rainfallsVec;
        for(int i = 0; i < m; i++){
            long y, r;
            cin >> y >> r;

            RainInfo ri(y, r, i);
            rainfallsVec.push_back(ri);
            rainfallsHash[y] = ri;
        }

        cin >> n;
        if (n == 0)
            break;

        if (first)
            first = false;
        else 
            cout << endl;

        SegmentTree st(rainfallsVec);
        for(int i = 0; i < n; i++){
            long y1, yy2, y2;
            cin >> y1 >> y2;

            long maxRain = st.query(y1 + 1, y2 - 1), y1Rain = 0, y2Rain = 0;
            //cout << "maxRain between " << (y1 + 1) << " and " << (y2 -1) << " is " << maxRain << endl;

            bool y1Known = rainfallsHash.find(y1) != rainfallsHash.end();
            if (y1Known)
                y1Rain = rainfallsHash.find(y1)->second.rainfall;

            bool y2Known = rainfallsHash.find(y2) != rainfallsHash.end();
            if (y2Known)
                y2Rain = rainfallsHash.find(y2)->second.rainfall;

            bool inBetweenKnown = (y2 - y1 == 1);
            auto itr1 = rainfallsHash.find(y1 + 1);
            if (itr1 == rainfallsHash.end()) inBetweenKnown = false;
            else {
                auto itr2 = rainfallsHash.find(y2 - 1);
                if (itr2 == rainfallsHash.end()) inBetweenKnown = false;
                else inBetweenKnown = (itr2->second.index - itr1->second.index) == ((y2 - 1) - (y1 + 1));
            }

            //cout << "inBetweenKnown = " << (inBetweenKnown? "true": "false") << endl;
            //cout << "y1Rain = " << y1Rain << ", y2Rain = " << y2Rain << endl;

            if (!y1Known && !y2Known) 
                cout << num(1) << "maybe" << endl;
            else
            if (y1Known && y2Known){
                if (y2Rain > y1Rain) cout << num(2) << "false" << endl;
                else {
                    if (inBetweenKnown) 
                        cout << num(3) << ((y2Rain > maxRain)? "true" : "false") << endl;
                    else 
                        cout << num(4) << ((y2Rain > maxRain)? "maybe" : "false") << endl;
                }
            }
            else if (y1Known) {
                cout << num(5) << ((y1Rain > maxRain)? "maybe" : "false") << endl;
            }
            else {
                // y2 known, y1 unknown
                cout << num(6) << ((y2Rain > maxRain)? "maybe": "false") << endl;
            }
        }
    }
    return 0;
}