import { useContext } from "react";
import { CounterContext } from "./context/CounterGlobalContextAPI";
import Button from "@mui/material/Button";

export default function CounterContextParent(props) {
  const { count, setCount } = useContext(CounterContext);

  return (
    <div>
      <h3>{props.cno} : Gloabl State (ContextAPI) Count: {count}</h3>

      <Button variant="outlined" onClick={() => setCount(count + 1)}>
        Increase
      </Button>

      <Button variant="outlined"  onClick={() => setCount(count - 1)}>
        Decrease
      </Button>
    </div>
  );
}