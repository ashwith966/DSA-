bool isPalindrome(int n) {
    int org=n;
    long long rev=0;
  int rem=0;

      
  if(n<0){
    return false;
  }
  else{

  
  
  while(n!= 0){
     rem=n%10;
    rev=rev*10+rem;
    n=n/10;

  }

  

  if(org==rev){
    return true;
  }
  else{
    return false;
  }
  }

}