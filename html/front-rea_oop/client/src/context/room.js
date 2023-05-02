import {useState, useContext,createContext} from 'react'

const RoomContext = createContext()

const RoomProvider = ({children}) => {
    const [roomdata,setRoomdata] = useState(
        
    );
    return (
        <RoomContext.Provider value={[roomdata, setRoomdata]}>
            {children}
        </RoomContext.Provider>
    );
};

const useRoom = () => useContext(RoomContext);

export { useRoom, RoomProvider};