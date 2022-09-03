class trip:

    # def info(self):
        
    #     self.a = input("Enter number of students:")
    #     self.b = input("Enter number of larger bus:")
    #     self.c = input("Enter number of set of larger bus:")
    #     self.d = input("Enter cost of larger bus:")
    #     self.e = input("Enter number of smaller bus:")
    #     self.f = input("Enter number of set of smaller bus:")
    #     self.g = input("Enter cost of smaller bus:")
    #     self.h = input("Enter number of drive:")


        # cout<<"Enter number of students:";
        # cin>>a;
        # cout<<"Enter number of larger bus:";
        # cin>>b;
        # cout<<"Enter number of set of larger bus:";
        # cin>>c;
        # cout<<"Enter cost of larger bus:";
        # cin>>d;
        # cout<<"Enter number of smaller bus:";
        # cin>>e;
        # cout<<"Enter number of set of smaller bus:";
        # cin>>f;
        # cout<<"Enter cost of smaller bus:";
        # cin>>g;
        # cout<<"Enter number of drive:";
        # cin>>h;
    

    def formula(self):
    
        
        a = int(input("Enter number of students:"))
        b = int(input("Enter number of larger bus:"))
        c = int(input("Enter number of set of larger bus:"))
        d = int(input("Enter cost of larger bus:"))
        e = int(input("Enter number of smaller bus:"))
        f = int(input("Enter number of set of smaller bus:"))
        g = int(input("Enter cost of smaller bus:"))
        h = int(input("Enter number of drive:"))



        y = a/f
        if(h>=y):
        
            x=0
            ans1=(d*x)+(g*y)
            aa=x
            bb=y
        
        else:
            ans1=0
        
        x=a/c
        if(h>=x):
        
            y=0
            ans2=(d*x)+(g*y)
            cc=x
            dd=y
        
        else:
            ans2=0
        
        if(ans1!=0):
        
            x=0
            y=h
            ans3=(d*x)+(g*y)
            ee=x
            ff=y
        
        if(ans2!=0):
        
            y=0
            x=h
            ans4=(d*x)+(g*y)
            gg=x
            hh=y
        
        p=a-(f*h)
        q=c-f
        x=p/q
        r=a-(c*h)
        s=f-c
        y=r/s
        ans5=(d*x)+(g*y)
        ii=x
        jj=y
        if(ans1==0):
        
            largest=ans2
            if(ans4<largest):
            
                largest=ans4
            
            elif(ans5<largest):
            
                largest=ans5
            
            if(largest==ans2):
                
                print(f"Your minimum cost is:{ans2}")
                print(f"So you choose:' {cc} ' larger bus and '{dd}' smaller bus")
                
                # cout<<"\nYour minimum cost is:"<<ans2;
                # cout<<"\nSo you choose '"<<cc<<"' larger bus and '"<<dd<<"' smaller bus";
            
            elif(largest==ans4):
            
                print(f"Your minimum cost is:{ans4}")
                print(f"So you choose:' {gg} ' larger bus and '{hh}' smaller bus")


                # cout<<"\nYour minimum cost is:"<<ans4;
                # cout<<"\nSo you choose '"<<gg<<"' larger bus and '"<<hh<<"' smaller bus";
            
            else:
            
                print(f"Your minimum cost is:{ans5}")
                print(f"So you choose:' {ii} ' larger bus and '{jj}' smaller bus")


                # cout<<"\nYour minimum cost is:"<<ans5;
                # cout<<"\nSo you choose '"<<ii<<"' larger bus and '"<<jj<<"' smaller bus";
            
        
        elif(ans2==0):
        
            largest=ans1
            if(ans3<largest):
            
                largest=ans4
            
            elif(ans5<largest):
            
                largest=ans5
            
            if(largest==ans1):
               
                print(f"Your minimum cost is:{ans1}")
                print(f"So you choose:' {aa} ' larger bus and '{bb}' smaller bus")    

                # cout<<"\nYour minimum cost is:"<<ans1;
                # cout<<"\nSo you choose '"<<aa<<"' larger bus and '"<<bb<<"' smaller bus";
            
            elif(largest==ans3):
            
                print(f"Your minimum cost is:{ans3}")
                print(f"So you choose:' {ee} ' larger bus and '{ff}' smaller bus")

                # cout<<"\nYour minimum cost is:"<<ans3;
                # cout<<"\nSo you choose '"<<ee<<"' larger bus and '"<<ff<<"' smaller bus";
            
            else:
            
                print(f"Your minimum cost is:{ans5}")
                print(f"So you choose:' {ii} ' larger bus and '{jj}' smaller bus")

                # cout<<"\nYour minimum cost is:"<<ans5;
                # cout<<"\nSo you choose '"<<ii<<"' larger bus and '"<<jj<<"' smaller bus";
            
        
if __name__ == "__main__":
    t = trip()
    # t.info()
    t.formula()


# int main()
# {
#     trip t;
#     t.info();
#     t.formula();
# }