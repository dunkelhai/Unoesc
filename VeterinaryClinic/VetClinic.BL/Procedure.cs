using System.ComponentModel.DataAnnotations;

namespace VeterinaryClinic.BL
{
    public class Procedure : IRegistroBancoDados
    {

        public int Id { get; set; }

        [Display(Name = "Procedure")]
        public string ProcedureName { get; set; }

        public string Observation { get; set; }

        public List<Attendance> Attendances { get; set; }
        

        public Procedure()
        {
        }

        public Procedure(int id, string procedureName, string observation)
        {
            Id = id;
            ProcedureName = procedureName;
            Observation = observation;
        }

        public override string ToString() =>
            string.Format("{0} - {1}", Id, ProcedureName);

        public bool Validate()
        {
            bool isValid = true;

            if (string.IsNullOrEmpty(ProcedureName)) isValid = false;

            return isValid;
        }
    }
}
