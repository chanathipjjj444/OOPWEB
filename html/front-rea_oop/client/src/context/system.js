import {useState, useContext,createContext} from 'react'

const SystemContext = createContext()

const SystemProvider = (props) => {
    const [system,setSystem] = useState({
        datanameHotel:"",
        datacheckin:"",
        datacheckout:"",
        datanumpeople:"",
    }
    );
    return (
        <SystemContext.Provider value={{system, setSystem}}>
            {props.children}
        </SystemContext.Provider>
    );
};

const useSystem = () => useContext(SystemContext);

export { useSystem, SystemProvider};