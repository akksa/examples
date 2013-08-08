#SKumar

import MySQLdb as mysql
import simplejson
def get_info():
    conn = mysql.connect(host='localhost', 
                        user='root',
                        passwd='root',
                        db='test')
    cur = conn.cursor()
    dis_role_code_q = 'select distinct role_code from k_train'
    q = 'select count(distinct RESOURCE), count(distinct mgr_id) , count(distinct ROLE_ROLLUP_1), count(distinct ROLE_ROLLUP_2), count(distinct ROLE_DEPTNAME) , count(distinct role_title), count(distinct ROLE_FAMILY_DESC), count(distinct ROLE_FAMILY), count(distinct ROLE_CODE), max(ROLE_CODE) from k_train where ROLE_CODE=%s'
    dis_role_code = []
    res = []
    col = ['RESOURCE', 'MGR_ID', 'ROLE_ROLLUP_1', 'ROLE_ROLLUP_2', 'ROLE_DEPTNAME', 'ROLE_TITLE', 'ROLE_FAMILY_DESC', 'ROLE_FAMILY', 'ROLE_CODE']
    cur.execute(dis_role_code_q)
    for row in cur.fetchall():
        dis_role_code.append(row[0])
    for i,x in enumerate(dis_role_code[:]):
        print 'Processing %d th data'%i
        q1 = q%x
        cur.execute(q1)        
        res.append(dict(zip(col,list(cur.fetchall())[0])))
    print len(res)
    #print res[:5]
    
    f=open('stat.dmp','w')
    simplejson.dump(res,f)
    f.close()
    print 'Done'

def read_info(fname = 'stat.dmp'):
    f=open(fname)
    res = simplejson.load(f)
    f.close()
    return res
    
if __name__ =='__main__':        
    col = ['RESOURCE', 'MGR_ID', 'ROLE_ROLLUP_1', 'ROLE_ROLLUP_2', 'ROLE_DEPTNAME', 'ROLE_TITLE', 'ROLE_FAMILY_DESC', 'ROLE_FAMILY', 'ROLE_CODE']
    #get_info()
    res = read_info()[:]
    for each in col:
        print each,' : ', max([x[each] for x in res])
    
    
        
    
