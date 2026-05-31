from sortedcontainers import SortedList

class segmentTree:
    def __init__(self):
        self.mx=50000
        self.seg=[0]*(self.mx<<2)
        self.st=SortedList([0, self.mx])
    def update(self, idx, val, p, l, r):
        #p->current tree node
        #range covered by current tree node -> [l,r]
        #idx-> position we want to update. val->new val
        if l==r:
            self.seg[p]=val
            return
        mid=(l+r)>>1 #divide by 2
        if idx<=mid:
            self.update(idx, val, p<<1, l, mid)
        else:
            self.update(idx, val, p<<1|1, mid+1, r)
        #left child -> p*2 -> p<<1
        #right child -> p*2+1 -> p<<1 |1
        self.seg[p]=max(self.seg[p<<1], self.seg[p<<1|1])
    def query(self, L, R, p, l, r):
        if L<=l and r<=R:
            return self.seg[p]
        mid=(l+r)>>1
        res=0
        if L<=mid:
            res=max(res, self.query(L,R,p<<1,l,mid))
        if R>mid:
            res=max(res, self.query(L,R,p<<1|1, mid+1, r))
        return res
class Solution(object):
    def getResults(self, queries):
        segment=segmentTree()
        segment.update(segment.mx, segment.mx, 1, 0, segment.mx)
        ans=[]
        for q in queries:
            if q[0]==1:
                x=q[1]
                idx=min(len(segment.st)-1, segment.st.bisect_right(x))
                r=segment.st[idx]
                l=segment.st[idx-1] if idx>0 else segment.st[0]
                segment.update(x, x-l, 1, 0, segment.mx)
                segment.update(r, r-x, 1, 0, segment.mx)
                segment.st.add(x)
            else:
                x, sz=q[1], q[2]
                idx=min(len(segment.st)-1, segment.st.bisect_right(x))
                pre=segment.st[0] if idx==0 else segment.st[idx-1]
                max_range=max(x-pre, segment.query(0,pre,1,0,segment.mx))
                ans.append(max_range>=sz)
        return ans
        '''
        p[i] -> position of nearest obstacle to the left of i
        d[i]=i-p[i] -> length of maximum blank interval ending at position i
        maximum value of d[i] in interval [o,x] is at least sz
        d[r] -> distance to nearest obstacle on left
        maintain d array dynamically.
        pre and nxt ->nearest object on left and right
        insert obstacle @ x -> update d[x] and d[nxt]
        [0,pre] -> consists of complete intervals -> directly using segment tree
        [pre, x] -> handled seperately by comp. length with sz
        to maintain ordered structure storing obstacles on both sides of x
        during insertion -> use balanced binary search tree
        '''