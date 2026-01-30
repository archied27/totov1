import { FormControl, Select, MenuItem, Box,  } from "@mui/material"
import { useState } from "react"

export default function MpvSelecter() 
{
    const [selected, setSelected] = useState('All')

    return (
        <Box p={2} display="flex" justifyContent="center" width="100%">
            <FormControl sx={{ minWidth: 100}}>
                <Select
                value={selected}
                onChange={(event) => { setSelected(event.target.value) }}
                displayEmpty
                inputProps={{ 'aria-label': 'Without label' }}
                >
                    <MenuItem value={"All"}>All</MenuItem>
                    <MenuItem value={"Movies"}>Movies</MenuItem>
                    <MenuItem value={"Shows"}>Shows</MenuItem>
                </Select>
            </FormControl>
        </Box>
    )
}