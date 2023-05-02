import {useState, useContext,createContext} from 'react'

const LastContext = createContext()

const LastProvider = ({children}) => {
    const [last,setLast] = useState(
        ""
    );
    return (
        <LastContext.Provider value={[last, setLast]}>
            {children}
        </LastContext.Provider>
    );
};

const useLast = () => useContext(LastContext);

export { useLast, LastProvider};