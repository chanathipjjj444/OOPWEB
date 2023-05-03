import {useState, useContext,createContext} from 'react'

const AddonsContext = createContext()

const AddonsProvider = ({children}) => {
    const [addonsdata,setAddonsdata] = useState(
        
    );
    return (
        <AddonsContext.Provider value={[addonsdata, setAddonsdata]}>
            {children}
        </AddonsContext.Provider>
    );
};


const useAddons = () => useContext(AddonsContext);


export { useAddons, AddonsProvider};