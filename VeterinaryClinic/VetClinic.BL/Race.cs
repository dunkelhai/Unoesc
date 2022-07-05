namespace VeterinaryClinic.BL
{
    public class Race : IRegistroBancoDados
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public int SpecieId { get; set; }
        public Specie Specie { get; set; }

        public Race()
        {
        }

        public Race(int id, string name, int specieId, Specie specie)
        {
            Id = id;
            Name = name;
            SpecieId = specieId;
            Specie = specie;
        }

        public bool Validate()
        {
            bool isValid = true;

            if (string.IsNullOrEmpty(Name)) isValid = false;

            return isValid;
        }
    }
}
