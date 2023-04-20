interface ButtonProps {
  label: string;
  onClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
  disabled?: boolean;
  small?: boolean;
  icon;
}

const Button = () => {
  return <div>Button</div>;
};

export default Button;
