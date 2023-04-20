interface ButtonProps {
  label: string;
  onClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
  disabled?: boolean;
}

const Button = () => {
  return <div>Button</div>;
};

export default Button;
