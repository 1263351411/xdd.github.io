## base64编码和解码
* 原理
    1. 计算机中，每个字节是8位的二进制数
    2. base64编码中，每一个8位的二进制数中只有后6位时有效字节，其他用0填充。
    3. 正常编码转成base64编码，满足3 * 8 = 24 = 4 * 6。即每3个字节的正常编码可以转成由4个字节组成的正常编码。
* base64编码表
![base64_001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/base64_001.jpg)  
### 编码图解：(参考维基百科)
* 3位的字节转成4位的base64字节
![base64_002](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/base64_002.jpg)  
* 2位的字节转成4位的base64字节，注意：补等号=  
![base64_003](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/base64_003.jpg)   
* 1位的字节转成4位的base64字节，注意：补等号  
![base64_004](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/base64_004.jpg) 

## 简单代码实现Python例子
````python
def xdd_base64():
    """
    base64,编码和解码
    :return:
    """
    strbase64 = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    dictbase64 = {k:i for i,k in enumerate(strbase64)}
    dictbase64[b"="[0]] = 0
    def base64Encode(stt:str)->bytes:# 编码
        """
            base64 编码，将字符串转成 base64格式的字符串
        :param stt:
        :return:
        """
        bstt = stt.encode(encoding="utf-8")
        # print(bstt,"====")
        k = 0
        count = len(bstt)
        barr = bytearray()
        for i in range(3,count,3):  #3*8=4*6
            units = bstt[k:i]
            barr.extend(getBytearry(units))
            k = i
        else:
            if k<count: #最后字节数不够3个字节。补0
                num = k-count+3
                endunits = bstt[k:] +b"\x00"*num #长度不够补0
                barr.extend(getBytearry(endunits))
                if num : barr[-num:] = b"=" * num  #末尾补等号

                # print(endunits)
        return bytes(barr)

    def getBytearry(nuits:bytes)->bytearray:
        """
        将3个8位的字节，转成4个6位的字节
        :param nuits:
        :return:
        """
        barr = []
        barrint = int.from_bytes(nuits,'big')
        for i in range(18,-1,-6):
            # 注意0x3F是16精制数，对应二精制数是11 1111 对应10进制数是63，与6个1的二进制数做与运算，相当于支取最后6个二进制数
            barr.append(strbase64[barrint>>i if i==18 else barrint>>i & 0x3F])
        return barr

    def base64Decode(stt:bytes)->bytes: #解码
        strarr = (stt[i-4:i] for i in range(4,len(stt)+1,4))
        arrby = bytearray()
        num = 0
        for nuits in strarr:
            rint = 0
            for k in nuits:
                if k == b"="[0]: num +=1 #统计尾部等号个数
                rint = (rint << 6) + dictbase64[k]
            arrby.extend(rint.to_bytes(3,"big"))
        while num: #去除尾部0字符
            arrby.pop()
            num -= 1
        return bytes(arrby)

    xdd_base64.encode = base64Encode
    xdd_base64.decode = base64Decode
    return xdd_base64
```` 
* 调用验证：
````python
import base64
stt = ["a","`",'ab','abc','abcd','ManMa',"教育a"]
for s in stt:
    xddbase = xdd_base64()
    destr = xddbase.encode(s)
    sysb64 = base64.b64encode(s.encode())
    print("base64编码：\t{}\t\t系統base64:\t{}".format(destr,sysb64))
    enstr = xddbase.decode(destr)
    print("base64解码:\t{}\t\t系統base64:\t{}".format(enstr,base64.b64decode(sysb64)))
    print()
````  
![base64_005](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/base64_005.jpg)


## java实现base64编码：
````java
package com.gdy.wts;
import java.util.Base64;

public class text3 {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String[] text = {"a","`","ab","abc","abcd"};
		for(String str :text){
			byte[] sysencode = Base64.getEncoder().encode(str.getBytes());
			System.out.println("系統base64编码为：\t"+ new String(sysencode));
			System.out.println("base64encode编码为:\t"+ new String(base64Encode(str)));
		}
		
	}
	private static final char[] toBase64 = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
    };
	
	/**
	 * base64编码
	 * @param str 需要编码的字符串
	 * @return byte[] base64编码 
	 */
	public static byte[] base64Encode(String str){
		
		byte[] bstr = str.getBytes();
		int mo = bstr.length%3;
		byte[] b64 = new byte[(mo==0?str.length()/3:str.length()/3+1)*4];
		int b64index = 0;
		int i=2;
		for(;i<bstr.length;i+=3){
			int temp = bstr[i-2]<<16 | bstr[i-1]<<8 | bstr[i];
			b64[b64index++] = (byte)toBase64[ temp>>18];
			b64[b64index++] = (byte)toBase64[ (temp>>12) & 0x3f];
			b64[b64index++] = (byte)toBase64[ (temp>>6) & 0x3f];
			b64[b64index++] = (byte)toBase64[temp & 0x3f];
		}
		if(mo!=0){
			int temp = 0;
			//补0
			for(int k=1;k<=mo;k++){
				temp |= bstr[i-3+k]<<(8*(3-k));
			}
			b64[b64index++] = (byte)toBase64[ temp>>18];
			b64[b64index++] = (byte)toBase64[ (temp>>12) & 0x3f];
			b64[b64index++] = (byte)toBase64[ (temp>>6) & 0x3f];
			b64[b64index++] = (byte)toBase64[temp & 0x3f];
			//替换等号
			for(int k=1;k<=3-mo;k++){
				b64[b64.length-k] = '=';
			}
		}
		return b64;
	}

}
````
* 运行结果如下：
![base64_006](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/base64_006.jpg)


