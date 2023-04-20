import { IconType } from "react-icons";

interface ButtonProps {
  label: string;
  onClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
  disabled?: boolean;
  small?: boolean;
  icon?: IconType;
}

const Button = () => {
  return <div>Button</div>;
};

export default Button;
