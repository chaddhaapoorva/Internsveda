const btns=[
{
    id:All,
    name:'All'
},
{
    id:CSE,
    name:'CSE'
},
{
    id:ECE,
    name:'ECE'
},
{
    id:Mechanical,
    name:'Mechanical'
},
{
    id:Management,
    name:'Management'
},
{
    id:Civil,
    name:'Civil'
}
]
const filters = [..new set(btns.map((btn)=>
{return btn}))]
